import subprocess
import pytest
import time
from tests import STREAMLIT_UPLOAD_FILE, STREAMLIT_DOWNLOAD_FILE


@pytest.fixture(scope="module")
def start_upload_streamlit_app():
    cmd = f"python -m streamlit run {STREAMLIT_UPLOAD_FILE} --server.headless true"
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(5)
    yield process
    process.terminate()
    process.wait()

@pytest.fixture(scope="module")
def start_download_streamlit_app():
    cmd = f"python -m streamlit run {STREAMLIT_DOWNLOAD_FILE} --server.headless true"
    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(5)
    yield process
    process.terminate()
    process.wait()

def test_upload_streamlit(subtests, start_upload_streamlit_app):
    with subtests.test(msg="streamlit up"):
        assert start_upload_streamlit_app.poll() is None, "Streamlit app failed to start"

    with subtests.test(msg="streamlit down"):
        start_upload_streamlit_app.terminate()
        time.sleep(2)
        assert start_upload_streamlit_app.poll() is not None, "Streamlit app failed to stop"

def test_download_streamlit(subtests, start_download_streamlit_app):
    with subtests.test(msg="streamlit up"):
        assert start_download_streamlit_app.poll() is None, "Streamlit app failed to start"

    with subtests.test(msg="streamlit down"):
        start_download_streamlit_app.terminate()
        time.sleep(2)
        assert start_download_streamlit_app.poll() is not None, "Streamlit app failed to stop"
