git status
echo "Uploading To GitHub"
git add .
echo -n "Write Commit For Push:"
read commitForGit
git commit -m $commitForGit
echo "### - Your Code Uploaded To GitHub Successfully - ####"

echo "Uploading To Heroku"
git push
git add .
echo -n "Write Commit For Push:"
read commitForGit
git commit -m $commitForGit
git push heroku master