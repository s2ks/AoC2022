#!/bin/bash

YEAR=$(date +%Y)
DAY=$(date +%-d)
SESSIONID=$(cat sessionid)
TEMPLATE=templ.py

get() {
	[[ -e day$DAY ]] || mkdir day$DAY

	curl "https://adventofcode.com/$YEAR/day/$DAY/input" \
		-H 'User-Agent: Mozilla/5.0' \
		-H "Cookie: session=$SESSIONID" \
		> day$DAY/input

	[[ -e day$DAY/pt1 ]] || cp $TEMPLATE day$DAY/pt1
	cd day$DAY && vim pt1
}

next() {
	if [[ ! -e pt1 ]]; then
		echo "no './pt1'"
		return 1
	fi

	if [[ -e pt2 ]]; then
		echo "./pt2 already exists"
		return 1
	fi

	cp pt1 pt2 && vim pt2
}

run() {
	if [[ ! -e input ]]; then
		echo "NO INPUT FILE"
		return 1
	fi

	[[ -e pt1 ]] && (echo -n "pt1: "; ./pt1 < input)
	[[ -e pt2 ]] && (echo -n "pt2: "; ./pt2 < input)
}
