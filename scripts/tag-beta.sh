#!/bin/sh

NEXT_VERSION=$(semantic-release print-version)
LAST_BETA_VERSION=$(git tag -l | grep "$NEXT_VERSION-beta.*" | tail -1)

if [[ ! $LAST_BETA_VERSION ]]; then
    NEXT_TAG="v$NEXT_VERSION-beta.1"
else
    LAST_BETA=$(echo "$LAST_BETA_VERSION" | grep -o "beta.*" | cut -d. -f2)
    NEXT_BETA=$((LAST_BETA + 1))
    NEXT_TAG="v$NEXT_VERSION-beta.$NEXT_BETA"
fi

git tag $NEXT_TAG
git push origin "$NEXT_TAG"