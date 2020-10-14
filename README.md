# Pythonic

파이썬스럽다

## Python Set Up - for mac OS

1. homebrew 섩치 --> 구글에서 쉽게 다운받을 수 있다.

   - \$ brew -v : brew 버전을 알 수 있다.
   - \$ brew update : brew 설치

2. python 설치

   - \$ brew install python3
   - \$ python3 : 설치를 확인할 수 있다.

3. pip 설치

   - \$ sudo easy_install pip
   - \$ pip3 install pip --upgrade
   - \$ pip3 --version
   - \$ pip3 freeze : 설치된 패키지를 확인할 수 있다.

4. 가상환경 pipenv 설치

   - \$ pip3 install pipenv
   - \$ pip3 install pipenv --upgrade
   - pipenv 명령어 : https://pipenv.pypa.io/en/latest/cli/#cmdoption-pipenv-rm

5. 프로젝트 폴더 만들기

   - \$ cd documents
   - \$ mkdir my_project
   - \$ cd my_project
   - \$ pipenv --python 3.8 : 가상환경을 만든다.
   - \$ pipenv shell : 가상환경 안으로 들어간다.

6. vs-code에서 flake8 선택 & 설치

   - linter은 작성한 코드에 에러가 생길 부분을 미리 감지한다.
   - shift + command + p --> python : select linter --> flake8 선택&설치 --> 해당 폴더에 .vscode 폴더가 생성된 것을 확인할 수 있다.
   - 해당 폴더에 .vscode 폴더가 생성된 것을 확인할 수 있다.

7. formatter-black

   - formatter은 코드를 보기좋게 format해준다.
   - \$ pipenv install black --dev --pre

8. .vscode안에 settings.json파일을 다음과 같이 수정한다.

   ```
   {
   "python.linting.pylintEnabled": false,
   "python.linting.flake8Enabled": true,
   "python.linting.enabled": true,
   "python.formatting.provider": "black",
   "python.linting.flake8Args": ["--max-line-length=88"]
   }
   ```

9. pipenv 명령어

   - \$ pipenv run python3 my_code.py : 가상환경에서 코드 실행하기
   - \$ pipenv install : 협업 프로젝트를 할때, 프로젝트의 모든 개발자들은 Git 저장소에 올려둔 Pipfile 파일과 Pipfile.lock 파일을 내려받은 후에 pipenv install 커맨드로 모든 패키지를 한 번에 설치할 수 있다.
   - \$ pipenv --where : Output project home information.
   - \$ pipenv graph : 프로젝트에 설치된 패키지들을 트리 구조로 시각화하여 보여준다.
   - \$ pipenv check : 보안 취약점이 있는 패키지가 설치되어 있는지 간단하게 체크 가능
