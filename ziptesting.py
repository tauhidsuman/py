#!/usr/bin/python
import zipfile
import os

z = zipfile.ZipFile("data/data", "w", zipfile.ZIP_LZMA)
for f in os.listdir("data/"):
	print(str(f))
	if f.endswith(".zip") or f == 'data': continue
	else: z.write("data/" + f, arcname=f)

z.close()