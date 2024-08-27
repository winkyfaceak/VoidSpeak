#!/bin/bash
# for MacOS
# Check if Homebrew is installed, if not then install it
if test ! $(which brew); then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
echo "Updating Homebrew..."

brew update

brew_apps=(
    python3
)

echo "Installing Homebrew packages..."
for app in "${brew_apps[@]}"; do
    brew install $app
done

echo "Now installing pip packages...."
pip3 install SpeechRecognition
pip3 install pocketsphinx
