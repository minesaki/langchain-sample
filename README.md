# LangChain sample 

Sample AI console application implemented with Python, LangChain (v0.3), and OpenAI API.  
This shows how to realize chat with history, function calling, and RAG.  

## Prerequisites

- Python 3.9 or above (required by LangChain v0.3) (tested with Python v3.13.0)
- OpenAI API account (< $0.01 at one execution)

## How to run

### Create .env file

Place .env file (contents are as follows) in the project root. It's loaded by run.sh.
```
export OPENAI_API_KEY=<Your OpenAI API Key>
```

### (For Windows users)

If you are a Windows user, <u>make sure that the MinGW toolchain is installed</u> before proceeding with the next step.  
(If not installed, you may see an error when `pip install langchain` due to missing some commands.)

1. Download MinGW-w64 (msys2-x86_64-yyyymmdd.exe) at https://www.msys2.org/
1. Install MinGW-w64
1. In MSYS2 terminal, run `pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain` with leaving all options at default values
1. Add `C:\msys64\ucrt64\bin` (or the path you specified) to the environment variable `PATH`

See https://code.visualstudio.com/docs/cpp/config-mingw for detail

### Install packages (required only for the first execution)

``` sh
pip install -r requirements.txt
```

### Execute

``` sh
./run.sh
```

#### Note

Sample 3 (RAG sample) generates embedding data, and the process may fail on Windows due to some error on the dependency (probably NumPy). In this case, please comment out `rag_sample()`.

In my case, the following errors occurred several times on numpy/core/getlimits.py.
```
RuntimeWarning: invalid value encountered in xxx
(xxx = exp2, nextafter, and log10)
```
_(I've faced no such issue on Mac so far.)_
