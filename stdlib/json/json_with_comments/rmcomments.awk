#!/usr/bin/env awk -f
# ======================================================================
#
# Very simple tool to remove Python-style comments
#
# Usage:
#     ./rmcomments.awk input-file
#
# Limitations:
# - Only remove stand-alone comments (those that are on a line by itself)
#
# ======================================================================

$1 !~ /#.*/
