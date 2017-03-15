#!/usr/bin/env python
from flask_script import Manager, Shell, Server
# from flask_assets import ManageAssets
from bookmark import create_app

app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())
# manager.add_command("assets", ManageAssets(app.assets_env))

manager.run()
