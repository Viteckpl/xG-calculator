# 🛠️ Problemy i rozwiązania / Issues & Solutions

## 🇵🇱 Napotkane trudności

1. **Model XGBoost wymagał natywnej biblioteki DLL**, co powodowało błędy w plikach `.exe`.  
   🔧 Rozwiązanie: Przejście na RandomForestClassifier z biblioteki `scikit-learn`.

2. **Brak zależności w PyInstaller** – model był tworzony z `sklearn`, ale PyInstaller nie pakował wszystkich podmodułów (`_forest`, `_tree`, itp.).  
   🔧 Rozwiązanie: Ręczne dodanie `--hidden-import` dla brakujących modułów.

3. **Problemy z ikoną** – niektóre `.ico` powodowały uszkodzenie `.exe` lub błędy w systemie Windows.  
   🔧 Rozwiązanie: Zastąpienie ikoną jednorożca z poprawnym kodowaniem i odpowiednim rozmiarem.

4. **Problemy z budową w OneDrive** – synchronizacja OneDrive psuła plik `.exe`.  
   🔧 Rozwiązanie: Przeniesienie projektu na lokalny dysk (`C:\xG`).

## 🇬🇧 Encountered issues

1. **XGBoost model required native DLL**, which broke `.exe` builds.  
   🔧 Solution: Switched to `RandomForestClassifier` from `scikit-learn`.

2. **Missing imports in PyInstaller** – model used `sklearn`, but PyInstaller didn’t include internal modules (`_forest`, `_tree`, etc.).  
   🔧 Solution: Manually added `--hidden-import` for required modules.

3. **Icon issues** – some `.ico` files broke the build or Windows preview.  
   🔧 Solution: Replaced with properly encoded unicorn icon in correct size.

4. **OneDrive corruption** – `.exe` files built in OneDrive folders were corrupted.  
   🔧 Solution: Moved project to local disk (`C:\xG`).
