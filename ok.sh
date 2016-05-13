git add .
git commit -m "sync"
git push
pelican content -o tianfudhe.github.io/
cd tianfudhe.github.io
git add .
git commit -a -m "sync"
git push