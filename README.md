# SUE AI Project - Predicting irregularities in Kubernetes networking logs

### Getting Started
#### Requirements
[Git](https://git-scm.com/downloads)
[DVC](https://dvc.org/)

#### Pulling repository
Pull the GitHub repository
```
git clone https://github.com/Fowthy/sueai.git
```

Configure DVC (AWS S3 bucket access keys)
```
dvc remote modify --local sue_2023 access_key_id TOKENHERE
```
```
dvc remote modify --local sue_2023 secret_access_key TOKENHERE
```

Pull all remote files
```
dvc pull -a
```

### Adding files
Add file to dvc
```
dvc add <FILENAME>
```

Push new files to remote
```
dvc push
```