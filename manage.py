from flask_script import Manager
from satcog.rest import create_app

manager = Manager(create_app())

if __name__ == '__main__':
    try:
        manager.run()
    except Exception:
        import traceback
        traceback.print_exc()
