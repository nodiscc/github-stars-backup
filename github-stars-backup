#!/bin/bash
# Description: Backup starred repositories for a Github user, output to JSON and plain text
# License: WTFPL
# Authors: nodiscc <nodiscc@gmail.com>
set -o errexit
set -o nounset

usage="$0 USERNAME OUTPUT_FILE"
username=${1:-}
outfile=${2:-}
tmpfile="github-stars.json"

##############################

# download starred repositories as JSON from the API, unauthenticated
# note that no error will be thrown if you exceed the API rate limit, but the results will be wrong
function download_starred() {
	i="1"
	response=$(curl "https://api.github.com/users/$username/starred?per_page=100\&page=$i")
	echo "$response" >| "$tmpfile"

	until [[ "$response" = "[

]" ]]; do
    	i=$(( "$i" +1 ))
    	response=$(curl "https://api.github.com/users/$username/starred?per_page=100\&page=$i")
    	echo "$response" >> "$tmpfile"
	done
}

function json_to_txt() {
	repos=$(grep full_name "$tmpfile" | cut -d"\"" -f4)
	for i in $repos; do
		echo "https://github.com/$i"
	done >| "$outfile"
}

function _main() {
	echo $tmpfile
	if [[ -z "$username" ]]; then
		echo -e "ERROR: no username provided"
		echo -e "USAGE: $usage"
		exit 1
	fi

	if [[ -z "$outfile" ]]; then
		echo -e "ERROR: no output file provided"
		echo -e "USAGE: $usage"
		exit 1
	fi

	download_starred
	json_to_txt
}

############################

_main