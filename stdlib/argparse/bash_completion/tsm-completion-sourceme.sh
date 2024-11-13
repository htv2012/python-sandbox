_tsm() {
    local cur=${COMP_WORDS[COMP_CWORD]}

        if [[ $COMP_CWORD -eq 1 ]]; then
            COMPREPLY=( $(compgen -W "apply-pending-changes authentication commands configuration customize data-access decommission discard-pending-changes failover-repository get-node-configuration-file help initialize jobs licenses login logout maintenance recommission register restart security sites start status stop topology user-identity-store version view-pending-changes" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'data-access' ]]; then
            COMPREPLY=( $(compgen -W "repository-access set-saml-delegation" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'data-access' ]] && [[ ${COMP_WORDS[2]} = 'repository-access' ]]; then
            COMPREPLY=( $(compgen -W "disable enable list" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'licenses' ]]; then
            COMPREPLY=( $(compgen -W "activate deactivate get-offline-activation-file get-offline-deactivation-file list" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'user-identity-store' ]]; then
            COMPREPLY=( $(compgen -W "get-group-mappings get-user-mappings list set-connection set-group-mappings set-user-mappings verify-group-mappings verify-user-mappings" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'sites' ]]; then
            COMPREPLY=( $(compgen -W "export import import-verified" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]]; then
            COMPREPLY=( $(compgen -W "kerberos list mutual-ssl open-id saml sspi trusted" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'kerberos' ]]; then
            COMPREPLY=( $(compgen -W "configure disable enable" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'sspi' ]]; then
            COMPREPLY=( $(compgen -W "disable enable" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'saml' ]]; then
            COMPREPLY=( $(compgen -W "configure disable enable export-metadata map-assertions" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'mutual-ssl' ]]; then
            COMPREPLY=( $(compgen -W "configure disable enable" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 4 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'mutual-ssl' ]] && [[ ${COMP_WORDS[3]} = 'disable' ]]; then
            COMPREPLY=( $(compgen -W "saml" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'open-id' ]]; then
            COMPREPLY=( $(compgen -W "configure disable enable map-claims" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 3 ]] && [[ ${COMP_WORDS[1]} = 'authentication' ]] && [[ ${COMP_WORDS[2]} = 'trusted' ]]; then
            COMPREPLY=( $(compgen -W "configure" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'maintenance' ]]; then
            COMPREPLY=( $(compgen -W "backup reindex-search restore send-logs ziplogs" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'jobs' ]]; then
            COMPREPLY=( $(compgen -W "list reconnect" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'configuration' ]]; then
            COMPREPLY=( $(compgen -W "export get set" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'security' ]]; then
            COMPREPLY=( $(compgen -W "get-external-ssl get-repository-ssl regen-internal-tokens set-external-ssl set-repository-ssl" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'topology' ]]; then
            COMPREPLY=( $(compgen -W "cleanup-coordination-service deploy-coordination-service list-nodes list-ports remove-nodes set-ports set-process toggle-coordination-service" -- $cur) )
        fi
    
        if [[ $COMP_CWORD -eq 2 ]] && [[ ${COMP_WORDS[1]} = 'failover-repository' ]]; then
            COMPREPLY=( $(compgen -W "-target" -- $cur) )
        fi
    
        # tsm apply-pending-changes
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "apply-pending-changes" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication kerberos configure
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "kerberos" ]] && [[ ${COMP_WORDS[3]} = "configure" ]]; then
            compopt -o nospace
            COMPREPLY=( $(compgen -o default -W "-h --help -k --keytab-file -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication kerberos disable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "kerberos" ]] && [[ ${COMP_WORDS[3]} = "disable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication kerberos enable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "kerberos" ]] && [[ ${COMP_WORDS[3]} = "enable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication list
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "list" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username -v --verbose" -- $cur) )
        fi

        # tsm authentication mutual-ssl configure
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "mutual-ssl" ]] && [[ ${COMP_WORDS[3]} = "configure" ]]; then
            COMPREPLY=( $(compgen -o default -W "-c --ca-cert -f --falback-to-basic -h --help -m --user-name-mapping -p --password -r --revocation-file --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication mutual-ssl disable saml
        if [[ $COMP_CWORD -ge 5 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "mutual-ssl" ]] && [[ ${COMP_WORDS[3]} = "disable" ]] && [[ ${COMP_WORDS[4]} = "saml" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication mutual-ssl enable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "mutual-ssl" ]] && [[ ${COMP_WORDS[3]} = "enable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication open-id configure
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "open-id" ]] && [[ ${COMP_WORDS[3]} = "configure" ]]; then
            COMPREPLY=( $(compgen -o default -W "-a --client-authentication -cs --client-secret -cu --config-url -h --help -i --client-id -id --ignore-domain -if --iframed-idp-enabled -ij --ignore-jwk -p --password -r --return-url --request-timeout -s --server -sn --custom-scope-name -u --username" -- $cur) )
        fi

        # tsm authentication open-id disable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "open-id" ]] && [[ ${COMP_WORDS[3]} = "disable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication open-id enable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "open-id" ]] && [[ ${COMP_WORDS[3]} = "enable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication open-id map-claims
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "open-id" ]] && [[ ${COMP_WORDS[3]} = "map-claims" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -i --id -p --password --request-timeout -s --server -sc --static-claim -u --username -un --user-name" -- $cur) )
        fi

        # tsm authentication saml configure
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "saml" ]] && [[ ${COMP_WORDS[3]} = "configure" ]]; then
            COMPREPLY=( $(compgen -o default -W "-a --max-auth-age -d --desktop-access -e --idp-entity-id -h --help -i --idp-metadata -m --mobile-access -p --password -r --idp-redirect-url --request-timeout -s --server -so --signout -ss --site-specific -su --signout-url -u --username" -- $cur) )
        fi

        # tsm authentication saml disable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "saml" ]] && [[ ${COMP_WORDS[3]} = "disable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication saml enable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "saml" ]] && [[ ${COMP_WORDS[3]} = "enable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication saml export-metadata
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "saml" ]] && [[ ${COMP_WORDS[3]} = "export-metadata" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --file -h --help -o --overwrite -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication saml map-assertions
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "saml" ]] && [[ ${COMP_WORDS[3]} = "map-assertions" ]]; then
            COMPREPLY=( $(compgen -o default -W "-d --display-name -e --email -h --help -o --domain -p --password -r --user-name --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication sspi disable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "sspi" ]] && [[ ${COMP_WORDS[3]} = "disable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication sspi enable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "sspi" ]] && [[ ${COMP_WORDS[3]} = "enable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm authentication trusted configure
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "authentication" ]] && [[ ${COMP_WORDS[2]} = "trusted" ]] && [[ ${COMP_WORDS[3]} = "configure" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -t --token-length -th --hosts -u --username" -- $cur) )
        fi

        # tsm commands
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "commands" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm configuration export
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "configuration" ]] && [[ ${COMP_WORDS[2]} = "export" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --output-config-file -h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm configuration get
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "configuration" ]] && [[ ${COMP_WORDS[2]} = "get" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -k --key -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm configuration set
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "configuration" ]] && [[ ${COMP_WORDS[2]} = "set" ]]; then
            COMPREPLY=( $(compgen -o default -W "--config-only -f --import-config-file -h --help -k --key -p --password --request-timeout -s --server --topology-only -u --username -v --value" -- $cur) )
        fi

        # tsm customize
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "customize" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help --header-logo --logo -p --password --request-timeout --restore-defaults -s --server --server-name --signin-logo -u --username" -- $cur) )
        fi

        # tsm data-access repository-access disable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "data-access" ]] && [[ ${COMP_WORDS[2]} = "repository-access" ]] && [[ ${COMP_WORDS[3]} = "disable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --repository-username --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm data-access repository-access enable
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "data-access" ]] && [[ ${COMP_WORDS[2]} = "repository-access" ]] && [[ ${COMP_WORDS[3]} = "enable" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --repository-password --repository-username --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm data-access repository-access list
        if [[ $COMP_CWORD -ge 4 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "data-access" ]] && [[ ${COMP_WORDS[2]} = "repository-access" ]] && [[ ${COMP_WORDS[3]} = "list" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm data-access set-saml-delegation
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "data-access" ]] && [[ ${COMP_WORDS[2]} = "set-saml-delegation" ]]; then
            COMPREPLY=( $(compgen -o default -W "-c --username-case -e --enabled -f --username-format -h --help -k --cert-key -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm decommission
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "decommission" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --force -h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm discard-pending-changes
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "discard-pending-changes" ]]; then
            COMPREPLY=( $(compgen -o default -W "--config-only -h --help -p --password --request-timeout -s --server --topology-only -u --username" -- $cur) )
        fi

        # tsm failover-repository -target
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "failover-repository" ]] && [[ ${COMP_WORDS[2]} = "-target" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password -r --preferred --request-timeout -s --server -t --target -u --username" -- $cur) )
        fi

        # tsm get-node-configuration-file
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "get-node-configuration-file" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --file -h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm initialize
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "initialize" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password -r --start-server --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm jobs list
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "jobs" ]] && [[ ${COMP_WORDS[2]} = "list" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -t --status -u --username" -- $cur) )
        fi

        # tsm jobs reconnect
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "jobs" ]] && [[ ${COMP_WORDS[2]} = "reconnect" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -i --id -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm licenses activate
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "licenses" ]] && [[ ${COMP_WORDS[2]} = "activate" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --license-file -h --help -k --license-key -p --password --request-timeout -s --server -t --trial -u --username" -- $cur) )
        fi

        # tsm licenses deactivate
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "licenses" ]] && [[ ${COMP_WORDS[2]} = "deactivate" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --license-file -h --help -k --license-key -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm licenses get-offline-activation-file
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "licenses" ]] && [[ ${COMP_WORDS[2]} = "get-offline-activation-file" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -k --license-key -o --output-dir -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm licenses get-offline-deactivation-file
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "licenses" ]] && [[ ${COMP_WORDS[2]} = "get-offline-deactivation-file" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -k --license-key -o --output-dir -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm licenses list
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "licenses" ]] && [[ ${COMP_WORDS[2]} = "list" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm login
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "login" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm logout
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "logout" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm maintenance backup
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "maintenance" ]] && [[ ${COMP_WORDS[2]} = "backup" ]]; then
            COMPREPLY=( $(compgen -o default -W "-d --append-date -f --file -h --help -i --description -k --skip-verification --override-disk-space-check -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm maintenance reindex-search
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "maintenance" ]] && [[ ${COMP_WORDS[2]} = "reindex-search" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm maintenance restore
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "maintenance" ]] && [[ ${COMP_WORDS[2]} = "restore" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --file -h --help -p --password -r --restart-server --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm maintenance send-logs
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "maintenance" ]] && [[ ${COMP_WORDS[2]} = "send-logs" ]]; then
            COMPREPLY=( $(compgen -o default -W "-c --case -e --email -f --file -h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm maintenance ziplogs
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "maintenance" ]] && [[ ${COMP_WORDS[2]} = "ziplogs" ]]; then
            COMPREPLY=( $(compgen -o default -W "-a --all -d --with-postgresql-data -f --file -h --help -i --description -l --with-latest-dump -m --minimumdate -o --overwrite -p --password --request-timeout -s --server -t --with-netstat-info -u --username" -- $cur) )
        fi

        # tsm recommission
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "recommission" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm register
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "register" ]]; then
            COMPREPLY=( $(compgen -o default -W "--file -h --help -p --password --request-timeout -s --server --template -u --username" -- $cur) )
        fi

        # tsm restart
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "restart" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm security get-external-ssl
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "security" ]] && [[ ${COMP_WORDS[2]} = "get-external-ssl" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm security get-repository-ssl
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "security" ]] && [[ ${COMP_WORDS[2]} = "get-repository-ssl" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm security regen-internal-tokens
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "security" ]] && [[ ${COMP_WORDS[2]} = "regen-internal-tokens" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm security set-external-ssl
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "security" ]] && [[ ${COMP_WORDS[2]} = "set-external-ssl" ]]; then
            COMPREPLY=( $(compgen -o default -W "--cert-file --chain-file --enabled -h --help --key-file -p --password --passphrase --protocols --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm security set-repository-ssl
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "security" ]] && [[ ${COMP_WORDS[2]} = "set-repository-ssl" ]]; then
            COMPREPLY=( $(compgen -o default -W "-e --enabled -h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm sites export
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "sites" ]] && [[ ${COMP_WORDS[2]} = "export" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --file -h --help -id --site-id -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm sites import
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "sites" ]] && [[ ${COMP_WORDS[2]} = "import" ]]; then
            COMPREPLY=( $(compgen -o default -W "-f --file -h --help -id --site-id -k --no-verify -m --override-schedule-mapper -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm sites import-verified
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "sites" ]] && [[ ${COMP_WORDS[2]} = "import-verified" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -id --site-id -p --password --request-timeout -s --server -u --username -w --import-job-dir" -- $cur) )
        fi

        # tsm start
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "start" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm status
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "status" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username -v --verbose" -- $cur) )
        fi

        # tsm stop
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "stop" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm topology cleanup-coordination-service
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "cleanup-coordination-service" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm topology deploy-coordination-service
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "deploy-coordination-service" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -n --nodes -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm topology list-nodes
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "list-nodes" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username -v --verbose" -- $cur) )
        fi

        # tsm topology list-ports
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "list-ports" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help --node-name -p --password --request-timeout -s --server --service-name -u --username" -- $cur) )
        fi

        # tsm topology remove-nodes
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "remove-nodes" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -n --node-names -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm topology set-ports
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "set-ports" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -i --instance -n --node-name -p --password -pn --port-name -pv --port-value --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm topology set-process
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "set-process" ]]; then
            COMPREPLY=( $(compgen -o default -W "-c --count -h --help -n --node -p --password -pr --process --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm topology toggle-coordination-service
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "topology" ]] && [[ ${COMP_WORDS[2]} = "toggle-coordination-service" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm user-identity-store get-group-mappings
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "get-group-mappings" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm user-identity-store get-user-mappings
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "get-user-mappings" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm user-identity-store list
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "list" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username -v --verbose" -- $cur) )
        fi

        # tsm user-identity-store set-connection
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "set-connection" ]]; then
            COMPREPLY=( $(compgen -o default -W "-b --bind -d --domain -h --hostname -kc --kerbconfig -kp --kerbprincipal -kt --kerbkeytab -l --port -lp --ldappassword -lu --ldapusername -n --nickname -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm user-identity-store set-group-mappings
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "set-group-mappings" ]]; then
            COMPREPLY=( $(compgen -o default -W "-b --basefilter -d --description -e --groupemail -h --help -m --member -n --groupname -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm user-identity-store set-user-mappings
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "set-user-mappings" ]]; then
            COMPREPLY=( $(compgen -o default -W "-c --certificate -dn --displayname -e --email -h --help -jp --jpegphoto -m --memberof -p --password --request-timeout -s --server -t --thumbnail -u --username -ub --basefilter -uu --ldapusername" -- $cur) )
        fi

        # tsm user-identity-store verify-group-mappings
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "verify-group-mappings" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username -v --verify" -- $cur) )
        fi

        # tsm user-identity-store verify-user-mappings
        if [[ $COMP_CWORD -ge 3 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "user-identity-store" ]] && [[ ${COMP_WORDS[2]} = "verify-user-mappings" ]]; then
            COMPREPLY=( $(compgen -f -d -o default -W "-h --help -p --password --request-timeout -s --server -u --username -v --verify" -- $cur) )
        fi

        # tsm version
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "version" ]]; then
            COMPREPLY=( $(compgen -o default -W "-h --help -p --password --request-timeout -s --server -u --username" -- $cur) )
        fi

        # tsm view-pending-changes
        if [[ $COMP_CWORD -ge 2 ]] && [[ ${COMP_WORDS[0]} = "tsm" ]] && [[ ${COMP_WORDS[1]} = "view-pending-changes" ]]; then
            COMPREPLY=( $(compgen -o default -W "--config-only -h --help -p --password --request-timeout -s --server --topology-only -u --username" -- $cur) )
        fi

}
complete -F _tsm tsm
