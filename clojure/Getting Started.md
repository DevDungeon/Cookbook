# Getting Started

First: 

- Install [Java](https://www.java.com/en/download/)
- Download `lein` or `lein.bat` from [http://leiningen.org/](http://leiningen.org/)

```bash
lein self-install
lein new <project>
cd <project>
vim project.clj # and add the following:
```

```clojure
(defproject leiningen.org "1.0.0"
  :description "Generate static HTML for http://leiningen.org"
  :dependencies [[enlive "1.0.1"]
                 [cheshire "4.0.0"]
                 [org.markdownj/markdownj "0.3.0-1.0.2b4"]]
  :main leiningen.web)
```

```bash
lein deps
```