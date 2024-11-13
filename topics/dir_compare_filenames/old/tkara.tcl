#!/usr/bin/env tclsh

package require sqlite3
package require Tclx
package require control

set version 0.1

namespace eval ::private {
    proc print_row {row_var} {
        upvar 1 $row_var row
        set id $row(id)
        set title $row(title)
        set singer $row(singer)
        puts [format "  %04d %-40s %-30s" $id $title $singer]
    }

    proc print_header {} {
        puts ""
        puts [format "%6s %-40s %-30s" "NUMBER" "TITLE" "SINGER"]
        puts [format "%6s %-40s %-30s" "======" "=====" "======"]
    }

    proc title_case {s} {
        set new {}
        foreach word $s {
            lappend new [string totitle $word]
        }
        return $new
    }

    proc prompt {} { return "\nkaraoke> " }
}

# Search and replace
proc r {search_for replace_with} {
    set sql "
        SELECT * FROM songs
        WHERE
            title like '%$search_for%'
            OR singer like '%$search_for%' "
    set map [list $search_for $replace_with]
    set answer ""
    ::db eval $sql {
        set new_title [string map $map $title]
        set new_singer [string map $map $singer]

        if {$answer != "a"} {
            puts ""
            puts "[format {%04d %-40s %s} $id $title $singer]"
            puts "[format {%04d %-40s %s} $id $new_title $new_singer]"

            control::do {
                puts -nonewline "(y)es, (n)o, (a)all ==> "
                flush stdout
                gets stdin answer
            } until {$answer == "y" || $answer == "n" || $answer == "a"}
        }

        if {$answer == "y" || $answer == "a"} {
            set sql "
                UPDATE
                    songs
                SET
                    title = '$new_title',
                    singer = '$new_singer'
                WHERE
                    id = '$id'"
            ::db eval $sql
        }
    }
}

# Search by title
proc t args {
    ::private::print_header
    ::db eval "SELECT * FROM songs WHERE title like '%${args}%'" row {
        ::private::print_row row
    }
}

# Search by singer
proc s args {
    ::private::print_header
    ::db eval "SELECT * FROM songs where singer like '%${args}%'" row {
        ::private::print_row row
    }
}

# Manage favorite
proc f {{user ""} {songid ""}} {
    if {$songid != ""} {
        # Add a new favorite
        set user [string totitle $user]
        set userid [::db eval "SELECT uid FROM users WHERE name = '$user'"]
        if {$userid == ""} {
            puts "\nUser $user is not in the system. Please add that user first."
        } else {
            set duplicated_songid [::db onecolumn "
                SELECT
                    sid FROM favorites
                WHERe
                    uid='$userid' AND sid='$songid'"]
            if {$duplicated_songid == ""} {
                set sql [subst {
                    INSERT INTO favorites (sid, uid)
                    VALUES ('$songid', '$userid')
                }]
                ::db eval $sql
            }
            f $user
        }
    } else {
        # List favorites for a person for for all
        set sql {
            SELECT
                users.name, songs.id, songs.title, songs.singer
            FROM
                users,favorites,songs
            WHERE
                users.uid = favorites.uid AND
                favorites.sid = songs.id
            }
        if {$user != ""} {
            append sql " AND users.name LIKE '$user'"
            append sql " ORDER BY songs.title"
        } else {
            append sql " ORDER BY users.name, songs.title"
        }

        puts "\n[format "%-8s  %-6s  %-40s %s" "USER" "NUMBER" "TITLE" "SINGER"]"
        puts "[format "%-8s  %-6s  %-40s %s" "====" "======" "=====" "======"]"
        ::db eval $sql {
            puts [format "%-8s    %04d  %-40s %s" $name $id $title $singer]
        }
    }
}

# Manage users
proc u {{user ""}} {
    if {$user == ""} {
        puts ""
        puts [format " %3s %s" "UID" "NAME"]
        puts [format " %3s %s" "===" "===="]
        ::db eval "SELECT uid, name FROM users ORDER BY name" {
            puts [format " %3d %s" $uid $name]
        }
    } else {
        # Add new user
        set namesFound [::db eval "SELECT name FROM users WHERE name = '$user'"]
        if {$namesFound == ""} {
            ::db eval "INSERT INTO users (name) VALUES ('$user')"
        } else {
            puts "\nUser $user is already in the system"
        }
    }
}

# Quit the program after cleaning up
proc q {} {
    ::db close
    exit
}

# Display help
proc help args {
    puts "
    f - Favorites listing or adding
    r - Replace <old> <new>
    s - Search by singer
    t - Search by title
    u - Show users
    q - Quit
    "
}

#
# Main
#
sqlite3 db karaoke.db
puts "
    Welcome to Karaoke Search version $version
    Written by Hai Vu
    "
help
commandloop -prompt1 ::private::prompt
db close

