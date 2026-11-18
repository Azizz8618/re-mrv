# Статус расшифровки СПО_тексты.pdf

Источник: `/home/azizz/Рабочий стол/Глиссада-6/СПО_тексты.pdf`, 335 стр.
Обновление: 2026-11-18.

| Стр. | Модуль | Расшифровка | Компиляция (dispak) | Комментарий |
|------|--------|-------------|---------------------|-------------|
| 2–3 | DOG — головной раздел | `docs/dog_head.txt` (113 стр.) | 0 ошибок | 4 ошибки старой расшифровки исправлены |
| 5–58 | DOG — основной модуль | `docs/dog2_compilable.txt` (1890 стр.) | 0 ошибок, `ЧИСЛО ОШИБ. ОПЕРАТОРОВ 0000` | 59 → 0 ошибок;Joint — `docs/dog_all.txt` |
| 59–101 | MRV — `MONAR`, PRINT-блок | `docs/mrv/mrv_core.txt` | 0 ошибок | PRINT1–12, PRINTS, PRINTK закрыли externals DOG; PRINT13–20 — в DOG стр.40–41 |
| 102–142 | REA | в работе | — | шапка READ (стр.102) |
| 143–167 | WRI | в работе | — | WRITE, RQTOCH, RUFCOM, ROTOCM, DATA; нужны WRITED/RQTOCHD/TTOCMD |
| 168–192 | RCD | `docs/rcd/` (4 подпрограммы) | 0 ошибок ×4 | не расшифровано: REAL (179–187), фрагменты 170–176, 178, 190 |
| 193–216 | WCD | `docs/wcd/` (2 подпрограммы) | 0 ошибок ×2 | не расшифровано: УСТ (193–201), TABLO (213–215) |
| 217–223 | M7B | `docs/m7b/` (4 подпрограммы) | 0 ошибок ×4 | RMTOB, IMTOB, RBTOM, IBTOM |
| 224–280 | PS | `docs/ps/ps_src.txt` (LPS1/PS1 + ONE/TWO) | 0 ошибок ×2 | не расшифровано: HD PS1–PS5, СБОР 1–5 (235–279) |
| 281–302 | DEB (Fortran) | `docs/deb/deb_fortran_head.txt` (только шапка) | — | `*assembler` не компилирует Fortran; SPIGUN/DERD/DEWR |
| 303–335 | DEB (МАДЛЕН) | `docs/deb/deb_src.txt` (560 стр., 16 подпрограмм) | 0 ошибок ×16 | таблица ссылок стр.335 списана |

## Внешние ссылки DOG (по данным `build/harness3.lst`)

| Символы | Источник | Статус |
|---------|----------|--------|
| `PRINT1…PRINT12`, `PRINTS`, `PRINTK` | MRV, стр.83–85 | ✅ закрыты в `docs/mrv/dog_plus_mrv.txt` |
| `PRINT13…PRINT20` | DOG, стр.40–41 | ❌ не в `dog_all.txt` |
| `SPIGUN`, `DERD`, `DEWR`, `RZAVAR` | DEB Fortran, стр.281–302 | ❌ Fortran не расшифрован |
| `PRPR2`, `PRV*` | не найдены в OCR | ❌ гипотеза: утраченные листинги |
| `WRITED`, `RQTOCHD`, `TTOCMD` | WRI, стр.143–167 | ⏳ агент в работе |
| `INFLD` | REA, стр.104–105 | ⏳ агент в работе |
| `DEBREG` | PROMON, стр.50 | ❌ не расшифрован |
| `*SYSTEM*`, `PLBEG`, `ASAVE*`, `ISO/GOST` | сервис ОС ДИСПАК | вне PDF |

## Проверка

```bash
cd /home/azizz/Yandex.Disk/re-mrv
bash scripts/check_all.sh
# OK docs/m7b/m7b_src.txt
# OK docs/ps/ps_src.txt
# ... 0 ошибок
```
