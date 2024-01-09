This code shows simple Dynaconf examples shared in the FlaskCon 2023 talk

To run an example set the FLASK_APP to the matching code you want to run.
For example:

>export FLASK_APP=flaskEnvConf

When using dynaconfFileConf you need to set the FLASK_ENV to the settings you want to load.
For example:

>export FLASK_ENV=production

To pass with VS Code's testing tool on dynaconfFileConf you need to set the FLASK_ENV to test in ./.env and modify ./vscode/settings.json

```json
{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.envFile": "${workspaceFolder}/.env"
}
```