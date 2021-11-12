import sys

import configparser
import atlassian_api_client


def main():
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    user = config['atlassian_api_client']['user']
    api_token = config['atlassian_api_client']['api_token']
    server = config['atlassian_api_client']['server']
    jira = atlassian_api_client.connect_to_jira_api(api_token, server, user)
    atlassian_api_client.get_pbi_data(jira, config['atlassian_api_client']['issue'])


if __name__ == '__main__':
    main()
