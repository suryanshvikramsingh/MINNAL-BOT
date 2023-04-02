if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/senapatibubai111/MINNAL-BOT.git /MINNAL-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MINNAL-BOT
fi
cd /MINNAL-BOT
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
