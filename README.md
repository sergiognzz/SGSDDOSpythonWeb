# HTTP Load Testing Script (Multiprocessing)

---

## 🇬🇧 English

This project is a simple Python-based tool for performing **controlled HTTP load testing** using multiprocessing.

⚠️ **Disclaimer**:
This tool is intended **only for testing systems you own or have explicit permission to test**. Unauthorized use against third-party services may be illegal.

### Features

* Multiprocessing support
* GET and POST requests
* Configurable number of workers
* Adjustable number of iterations
* Colored console output

### Usage

```bash
python3 script.py <target_url> [num_processes] [iterations]
```

Example:

```bash
python3 script.py https://example.com 5 20
```

### Installation

```bash
pip install -r requirements.txt
```

### Notes

* Use responsibly and ethically
* Monitor your system resources during tests

---

## 🇪🇸 Español

Este proyecto es una herramienta en Python para realizar **pruebas de carga controladas** utilizando multiprocessing.

⚠️ **Aviso**:
Solo debe usarse en sistemas propios o con autorización explícita. El uso no autorizado puede ser ilegal.

### Características

* Soporte para multiprocessing
* Peticiones GET y POST
* Número de procesos configurable
* Iteraciones ajustables
* Salida en consola con colores

### Uso

```bash
python3 script.py <target_url> [num_processes] [iterations]
```

Ejemplo:

```bash
python3 script.py https://example.com 5 20
```

### Instalación

```bash
pip install -r requirements.txt
```

### Notas

* Usar de forma responsable
* Monitorizar recursos del sistema

---

## 🇮🇹 Italiano

Questo progetto è uno strumento Python per eseguire **test di carico controllati** utilizzando multiprocessing.

⚠️ **Avviso**:
Utilizzare solo su sistemi propri o con autorizzazione esplicita. L’uso non autorizzato può essere illegale.

### Funzionalità

* Supporto multiprocessing
* Richieste GET e POST
* Numero di processi configurabile
* Iterazioni regolabili
* Output colorato

### Utilizzo

```bash
python3 script.py <target_url> [num_processes] [iterations]
```

Esempio:

```bash
python3 script.py https://example.com 5 20
```

### Installazione

```bash
pip install -r requirements.txt
```

### Note

* Usare in modo responsabile
* Monitorare le risorse del sistema

---

## 🇫🇷 Français

Ce projet est un outil Python permettant d’effectuer des **tests de charge contrôlés** en utilisant le multiprocessing.

⚠️ **Avertissement** :
À utiliser uniquement sur des systèmes dont vous êtes propriétaire ou avec autorisation explicite.

### Fonctionnalités

* Support du multiprocessing
* Requêtes GET et POST
* Nombre de processus configurable
* Itérations ajustables
* Sortie console colorée

### Utilisation

```bash
python3 script.py <target_url> [num_processes] [iterations]
```

Exemple :

```bash
python3 script.py https://example.com 5 20
```

### Installation

```bash
pip install -r requirements.txt
```

### Notes

* Utiliser de manière responsable
* Surveiller les ressources système

---

## 📦 Requirements

Create a file named `requirements.txt` with the following content:

```txt
requests
termcolor
```
