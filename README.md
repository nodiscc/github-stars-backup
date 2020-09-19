# github-stars-backup

Backup a list of github starred repositories for the specified user.

### Python version

- The python version requires that you generate a [Personal Access Token](https://github.com/settings/tokens) with the scope `read:user`
- The token must be exported to the `GITHUB_ACCESS_TOKEN` environment variable
- It outputs a JSON file containing the name, description, url, homepage, language number of open issues/stars of each starred repository
- The rate limit for authenticated API requests is 5000 requests/hour.

#### Installation

```bash
# install requirements in a virtualenv
python3 -m venv ~/.local/venv
source ~/.local/venv/bin/activate
pip3 install PyGithub

# clone the repository
git clone https://gitlab.com/nodiscc/github-stars-backup
cd github-stars-backup
```

#### Usage

```bash
./github-stars-backup.py --help
  USAGE: ./github-stars-backup.py USERNAME OUTPUT_FILE
  GITHUB_ACCESS_TOKEN must be declared in the environment, see https://github.com/settings/tokens

export GITHUB_ACCESS_TOKEN=aaaabbbbccccddddeeefffggghhhiijjj
./github-stars-backup.py nodiscc github-stars-backup.json
```

```json
$ cat github-stars-backup.json
{
  "ayyi/samplecat": {
    "name": "ayyi/samplecat",
    "description": "SampleCat is a a program for cataloguing and auditioning audio samples.",
    "url": "https://github.com/ayyi/samplecat",
    "homepage": "http://ayyi.github.io/samplecat/",
    "language": "C",
    "open_issues": 15,
    "stars": 33
  },
  ...
}
```


### Bash version (legacy)

- The (unmaintained) bash version does not require API authentication.
- It doesn't handle errors well, output will be wrong when the API rate limit is exceeded. The [rate limit](https://developer.github.com/v3/#rate-limiting) for unauthenticated requests is only 60 requests/hour.
- An intermediary JSON file containing the full API request results will be stored at `github-stars.json`
- The final output is a plain text list of starred repositories

```bash
USAGE: ./github-stars-backup.sh USERNAME OUTPUT_FILE

$ ./github-stars-backup.sh nodiscc github-stars.txt
$ cat github-stars.txt
```
```
https://github.com/eliasgranderubio/dagda
https://github.com/banyanops/collector
https://github.com/building5/ansible-vault-tools
...
```
