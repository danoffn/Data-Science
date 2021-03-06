#  Ejercicios Data Science Desafío Latam

## Virtual Environments

Permiten crear ambientes locales de trabajo, instalando paquetes localmente, etc.

```bash
python -m venv venv # venv directorio
source venv/bin/activate # activar environment
which python # verificar environment
pip install pandas
pip install numpy
pip install matplotlib
pip install scipy
pip install watermark
pip install seaborn
pip install statsmodels
pip install sklearn
pip install missingno
pip install factor_analyzer
pip install 'pygam===0.5.2' # version necesaria para desafío 2 - ML
pip install imbalanced-learn
pip install pydotplus # requerido por funciones personalizadas afx
pip install xlrd # Manipular xlsx
deactivate # para salir del environment

```

### Virtual environments with jupyter

```bash
pip install ipykernel
python -m ipykernel install --user --name=venv
```

### Habilitar jupyter extensions

```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

## Usando python in Anaconda

```bash
source /opt/anaconda/bin/activate
which python
python leerPanda.py #para ejecutar
conda deactivate #para salir
```
