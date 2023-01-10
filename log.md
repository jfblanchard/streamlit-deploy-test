# Streamlit deploy log


* GUI compoenents working well
* Dog/cat classifier model not training, error below

RuntimeError: This app has encountered an error. The original error message is redacted to prevent data leaks. 
Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback
File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 565, in _run_script
    exec(code, module.__dict__)
File "/app/streamlit-deploy-test/app.py", line 32, in <module>
    learn = train_image_classifier(path)
File "/app/streamlit-deploy-test/app.py", line 19, in train_image_classifier
    learn.fine_tune(1)
File "/home/appuser/venv/lib/python3.9/site-packages/fastai/callback/schedule.py", line 165, in fine_tune
    self.fit_one_cycle(freeze_epochs, slice(base_lr), pct_start=0.99, **kwargs)
