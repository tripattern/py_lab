# Atlassian Lab
#### Access with API Token
* Create API Token
    * https://id.atlassian.com/manage-profile/security/api-tokens
* Create file with access info (filename.txt)
```
user
token
jira_url
```
* Input as piped command line args to python script accessing atlassian
```
cat ~/path/filename.txt | xargs python ./atlass/list_of_issues
```