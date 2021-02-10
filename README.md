# wiki
Application for the searching and reading Wikipedia articles from the console.
It is a wrapper for the wikipedia package from https://pypi.org/project/wikipedia/

## REQUIREMENTS

- python 3
- wikipedia

The wikipedia package can be installed with

```
pip install wikipedia 
```

## Usage

```
./wiki
```
It will find for you a random Wikipedia article.

If you run 
```
./wiki <query> 
./wiki "phrase" 
```
than it will try to find the artical by *query* or *phrase* key. Finally it suggest you to choose
the article from the best matches.