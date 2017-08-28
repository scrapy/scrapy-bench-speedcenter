import argparse
import json
import platform


def main():
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('python_versions', help='comma separated')
    arg('scrapy_versions', help='comma separated')
    args = parser.parse_args()
    initial_data = [
        {
            "fields": {
                "repo_type": "H",
                "name": "scrapy",
                "commit_browsing_url":
                    "https://github.com/scrapy/scrapy/commit/{commitid}",
                "repo_user": "",
                "track": True,
                "repo_pass": "",
                "repo_path": "https://github.com/scrapy/scrapy"
            },
            "model": "codespeed.project",
            "pk": 1
        },
        {
            "fields": {
                "project": 1,
                "name": "default"
            },
            "model": "codespeed.branch",
            "pk": 1
        }
    ]

    pk = 1
    cpu = platform.processor()
    os = platform.system()
    for py_version in args.python_versions.split(','):
        for scrapy_version in args.scrapy_versions.split(','):
            initial_data.append({
                "fields": {
                    "kernel": "",
                    "memory": "",
                    "os": os,
                    "name":
                        "{} Scrapy {}".format(py_version, scrapy_version),
                    "cpu": cpu,
                },
                "model": "codespeed.environment",
                "pk": pk,
            })
            pk += 1
    print(json.dumps(initial_data, indent=True))


if __name__ == '__main__':
    main()
