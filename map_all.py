# -*- coding: utf-8 -*-
import cham_diem_core

students = cham_diem_core.STUDENT_RESULTS
for s in students:
    stt = s['stt']
    name = s['name']
    code = s['code']
    print(f"{stt:2d} | {name:22s} | {code}")
