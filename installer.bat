@echo off
echo Tworzę .exe z kalkulatorem xG...
pyinstaller ^
  --onefile ^
  --add-data "model\model_xg_rf.pkl;model" ^
  --hidden-import sklearn ^
  --hidden-import sklearn.ensemble._forest ^
  --hidden-import sklearn.tree._tree ^
  --hidden-import sklearn.tree._splitter ^
  --hidden-import sklearn.tree._criterion ^
  --hidden-import sklearn.utils._cython_blas ^
  --icon unicorn.ico ^
  xg_gui_rf_validated_final.py
echo Gotowe! Sprawdź folder dist\
pause
