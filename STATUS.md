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
| **отд. PDF, 1–7** | **ТЕСТ СВЯЗИ С СМ-2** (3 модуля МАДЛЕН + Fortran + дамп) | `docs/sm2_test/` (`sm2_wint.txt`, `sm2_program.txt`, `sm2_wcnt.txt`, `sm2_test_run.txt`, `sm2_combined.txt`) | **0 ошибок ×3 + запуск: E50=0, `КОНЕЦ ЗАДАЧИ`** | `ТЕСТ_СВЯЗЬ_СМ-2.pdf`; 43→0 ошибок в W INT; адреса сверены с таблицей ссылок; стр.6 — Fortran `PRNT`, стр.7 — дамп; подробности `docs/sm2_test/README.md` |

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

`docs/integration/mrv_all.txt` (8281 строка, 27 исходников, **50 модулей**) —
максимальный рабочий набор: DOG (головной + основной, включая PRINT13…20)
+ MRV/PROMON (PRINT1…12, PRINTS, PRINTK) + REA + WRI (6) + RCD (9) + WCD (6)
+ M7B (4) + PS (7) + DEB МАДЛЕН (14). Fortran DEB (`*system`) собирается
отдельно и в обёртку не входит.

Компиляция: `bash scripts/build_one.sh docs/integration/mrv_all.txt MRVALL
build/integration` — 0 ошибок; в полном листинге
`build/integration/mrv_all_full.lst` все 50 модулей имеют
`ЧИСЛО ОШИБ. ОПЕРАТОРОВ 0000`. Загрузчик (`build/integration/mrv_all.lst`):
PROGRAM 01000, DOG 02000, СВОБОД 20023. PRINT13…20 закрыты (в списке
`ОТСУТСТВУЕТ` отсутствуют). Остаются незакрытыми 25 символов:
`PRINT1…7`, `PRINT9…12`, `PRINTS`, `PRINTK`, `PRPR2`, `PRV`, `PRV1…3`,
`SPIGUN`, `DERD`, `DEWR`, `RZAVAR`, `RQTOCMD`, `BUFCOM`, `ОКНО`
(кириллица); предупреждения `НЕВЕРНАЯ ДЛИНА LINK / *DEBAR*`.
Остальные модули оттранслированы, но загрузчиком в задачу не включены
(нет `XTS`/`CALL` из PROGRAM и DOG) — это свойство загрузчика dispak.

Для снятия конфликта `ENTRY PROGRAM` (6 модулей PS: ONE, СБОР 1–4,
HD PS1) эти строки заменены комментариями; без этого загрузчик грузит
по 01000 последний такой модуль вместо головного PROGRAM. Подробности,
порядок модулей, адреса и исключённые исходники —
`docs/integration/README.md`. `mrv_all.txt` добавлен в `docs/SOURCES.txt`.

### Тест связи с СМ-2 и запуск

`docs/sm2_test/` — расшифровка 7 стр. `ТЕСТ_СВЯЗЬ_СМ-2.pdf` (МАДЛЕН
`W INT` / `PROGRAM` / `W'`, плюс Fortran `PRNT` на стр.6 и дамп стр.7).
Отдельные модули и joint-вариант `sm2_combined.txt` компилируются с
0 ошибок; запуск через `dispak -t` завершается `КОНЕЦ ЗАДАЧИ`, `E50 = 0`
(`build/sm2_test/sm2_trace.txt`). Адреса совпали с таблицей ссылок PDF
(`OUTFLD1=0066₈`, `CNTPC1=0071₈`, `M=0100₈`).

МРВ целиком (`build/integration/mrv_all.b6`) тоже запущен с `-t`:
`КОНЕЦ ЗАДАЧИ`, `E50 = 0`, трасса — `build/integration/mrv_all_trace.txt`.

`build/integration/mrv_sm2.b6` — формальная joint-сборка МРВ + теста:
компилируется без ошибок, но загрузчик dispak берёт `PROGRAM` теста
(`START`, WINT, W) и не кладёт в память модули МРВ; единственная
незакрытая ссылка — `PRNT` (Fortran, отдельная сборка).

Предыдущая промежуточная сборка — `docs/integration/dog_mrv_wri.txt`
(DOG + WRI, `build/integration/final_joint.lst`); в ней PRINT13…20 ещё
были незакрытыми.

## Проверка

```bash
cd /home/azizz/Yandex.Disk/re-mrv
bash scripts/check_all.sh
# OK docs/m7b/m7b_src.txt
# OK docs/ps/ps_src.txt
# OK docs/ps/sbor1.txt .. sbor4.txt, docs/ps/hdps1.txt (build/ps_more/)
# ... 0 ошибок
```

## Обследование re-glissade (18.11.2026)

Подробный отчёт — `docs/re_glissade_findings.md`. Готового паспорта/задания
для зоны 4000(8) тома 2348 и исходников МРВ в re-glissade **нет**; все
рабочие сценарии записи используют PERSO-зону 2700(8)
(`*perso:402700`, `TOOLS/install-2348.sh`). Механику можно перенести:
`python3 TOOLS/build-dialog.py <work> 4000` даёт `*perso:404000`, а в
`install-2348.sh` нужно заменить `--start=1472` на `--start=2048`.
`ВХО 4000` в `docs/2053_passports.txt` — адрес входа, не зона диска.

## Паспорт МРВ на системных дисках (18.11.2026)

Отчёт — `docs/passport/MRV_PASSPORT.md`. Паспорта `МРВ`/`MRV` **не найден**:
прогнан `besmtool pass` по ~50 образам в 4 каталогах (2053, 2253, 2453,
2113, 2048/2248/2348 и др.), проверен «журнал паспортов» диска 2053
(зоны 0766, 0774, 1224, 1624), поиск `MRV/МРВ/MPB/MRB/NEWDOG/K71` по
содержимому дисков и OCR `СПО_тексты.pdf` (0 упоминаний `ПАСПОРТ`),
бэкапы 2053/2253 и каталог АРФА (отсутствует).

Единственный найденный паспорт с именем `-DOG-` — **не МРВ**: служебная
задача «АНТИАНИС», `ШИФР 113300000000`, `ВРЕ 3`, `ВХО 7`, `ЛИС 0`,
`ЕВ 4`, введена 06.06.80 (журнал 2053, зоны 0774.0650 / 1224.0700 /
1624.0710). У МРВ же `PROGRAM` по 01000₈, `DOG` по 02000₈, вход `NEW DOG`.

Запуск МРВ идёт не через паспорт ДИСПАК, а через колоду МАДЛЕН:
`cd build/integration && dispak -t mrv_all.b6` → `КОНЕЦ ЗАДАЧИ`, `E50 = 0`.
