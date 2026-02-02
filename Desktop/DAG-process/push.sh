#!/bin/bash
# push.sh — commit and push everything to GitHub


git add .
git commit -m "Rename project folder"
git push

git commit -m "Update Airflow DAGs and Docker setup"

git remote add origin https://github.com/E-creator513/EL-process8.git

git push origin $(git rev-parse --abbrev-ref HEAD)
