# Статус расшифровки СПО_тексты.pdf

Источник: `/home/azizz/Рабочий стол/Глиссада-6/СПО_тексты.pdf`, 335 стр.
Обновление: 2026-11-18.

| Стр. | Модуль | Расшифровка | Компиляция (dispak) | Комментарий |
|------|--------|-------------|---------------------|-------------|
| 2–3 | DOG — головной раздел | `docs/dog_head.txt` (113 стр.) | 0 ошибок | 4 ошибки старой расшифровки исправлены |
| 5–58 | DOG — основной модуль | `docs/dog2_compilable.txt` (1890 стр.) | 0 ошибок, `ЧИСЛО ОШИБ. ОПЕРАТОРОВ 0000` | 59 → 0 ошибок;Joint — `docs/dog_all.txt` |
| 59–101 | MRV — `MONAR`, PRINT-блок | `docs/mrv/mrv_core.txt` | 0 ошибок | PRINT1–12, PRINTS, PRINTK закрыли externals DOG; PRINT13–20 закрыты в `docs/print13/dog_all_v2.txt` (DOG, стр.40–41) |
| 102–142 | REA — `READ` | `docs/rea/rea_src.txt` (1513 стр.) | 0 ошибок, `ЧИСЛО ОШИБ. ОПЕРАТОРОВ 0000` | 49 → 0 ошибок; 367 селекторов вместо меток, таблицы перенесены перед кодом (однопроходный транслятор) |
| 143–167 | WRI | `docs/wri/wri_src.txt` (1078 стр., 6 модулей) | 0 ошибок ×6 | WRITE, RQTOCM, RUFCOM, WRITE D, ROTOCM D, DATA; `WRITED` закрыт. В скане пропущены оригинальные стр.161–162 |
| 168–192 | RCD | `docs/rcd/` (9 подпрограмм) | 0 ошибок ×9 | REAL, RSTREG (стр.170+172–174), R D TAB, R48COD, R16COD расшифрованы; стр.171, 190 — схемы/таблицы, кода нет |
| 193–216 | WCD | `docs/wcd/` (6 подпрограмм) | 0 ошибок ×6 | 2026-11-18: добавлены УСТ (193–197), REAL (198–201), 16COD (206–208), TABLO (213–216); стр.205, 212, 216 — таблицы ссылок (кода нет) |
| 217–223 | M7B | `docs/m7b/` (4 подпрограммы) | 0 ошибок ×4 | RMTOB, IMTOB, RBTOM, IBTOM |
| 224–280 | PS | `docs/ps/ps_src.txt` (LPS1/PS1 + ONE/TWO), `docs/ps/sbor{1,2,3,4}.txt`, `docs/ps/hdps1.txt` | 0 ошибок ×7 | 2026-11-18: добавлены СБОР 1–4 и HD PS1 (`build/ps_more/`); не расшифровано: HD PS2–PS5, LPS2–LPS5, PS2/PS3. Отдельного «СБОР 5» нет — стр.277–279 = СБОР 4 |
| 281–302 | DEB (Fortran) | `docs/deb/deb_fortran_src.txt` (654 стр., SPIGUN + DEWR/PZAVAR/DERD) | 0 ошибок через `*system` (Fortran-Dubna), `ЧИСЛО ОШИБ. ОПЕРАТОРОВ 0000` | стр.281–291 расшифрованы полностью; стр.294–301 (VIN/VIN16/VINRL/VTKOM/VTIS/VTB/WRDESK) не расшифрованы; `RZAVAR` = `PZAVAR` (OCR-гипотеза) |
| 303–335 | DEB (МАДЛЕН) | `docs/deb/deb_src.txt` (560 стр., 16 подпрограмм) | 0 ошибок ×16 | таблица ссылок стр.335 списана |

## Внешние ссылки DOG (по данным `build/harness3.lst`)

| Символы | Источник | Статус |
|---------|----------|--------|
| `PRINT1…PRINT12`, `PRINTS`, `PRINTK` | MRV, стр.83–85 | ✅ закрыты в `docs/mrv/dog_plus_mrv.txt` |
| `PRINT13…PRINT20` | DOG, стр.40–41 | ✅ закрыты в `docs/print13/dog_all_v2.txt`, 0 ошибок |
| `SPIGUN`, `DERD`, `DEWR`, `PZAVAR` | DEB Fortran, стр.281–291 | ✅ определены в `docs/deb/deb_fortran_src.txt` (0 ошибок); `RZAVAR` — ошибочная OCR-гипотеза, в скане `PZAVAR` |
| `PRPR2`, `PRV*` | не найдены в OCR | ❌ гипотеза: утраченные листинги |
| `WRITED` | WRI, стр.156 | ✅ закрыт в совместной сборке |
| `RQTOCMD`, `TTOCMD` | WRI (`RQTOCM`, `ROTOCMD`, `TTOCM D`) | ⚠️ точного совпадения нет — нужного подтверждения |
| `INFLD` | REA, стр.104–105 | ✅ определено в `docs/rea/rea_src.txt` |
| `DEBREG` | PROMON, стр.50 | ❌ не расшифрован |
| `*SYSTEM*`, `PLBEG`, `ASAVE*`, `ISO/GOST` | сервис ОС ДИСПАК | вне PDF |

## Итоговая совместная сборка

`docs/integration/dog_mrv_wri.txt` = DOG (головной + основной) + MRV
PRINT-блок + WRI (6 модулей). Компиляция и загрузка через `dispak`
проходят без ошибок (`build/integration/final_joint.lst`).

PRINT13…20 расшифрованы по стр.40–41 и вставлены в
`docs/print13/dog_all_v2.txt` (1956 перфокарт, 0 ошибок); строки
`ОТСУТСТВУЕТ PRINT13…PRINT20` из таблицы загрузчика исчезли.
Остаются незакрытыми: `PRPR2`, `PRV*`, `RQTOCMD`, `BUFCOM`,
`ОКNО` (латиница/кириллица), плюс символы сервиса ОС ДИСПАК.

## Проверка

```bash
cd /home/azizz/Yandex.Disk/re-mrv
bash scripts/check_all.sh
# OK docs/m7b/m7b_src.txt
# OK docs/ps/ps_src.txt
# OK docs/ps/sbor1.txt .. sbor4.txt, docs/ps/hdps1.txt (build/ps_more/)
# ... 0 ошибок
```
