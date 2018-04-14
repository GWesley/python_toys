#!/bin/zsh
UDID=$(idevice_id -l) xcode-select -print-path
xcodebuild -project WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test