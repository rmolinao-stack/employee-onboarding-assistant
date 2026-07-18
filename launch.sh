# Asegura que la carpeta de entregables exista antes de lanzar los tests
mkdir -p entregables

echo 11 | python -X utf8 main.py > ./entregables/DEMO_AS11.TXT
echo 12 | python -X utf8 main.py > ./entregables/DEMO_AS12.TXT
echo 21 | python -X utf8 main.py > ./entregables/DEMO_AS21.TXT
echo 22 | python -X utf8 main.py > ./entregables/DEMO_AS22.TXT
echo 31 | python -X utf8 main.py > ./entregables/DEMO_AS31.TXT
echo 41 | python -X utf8 main.py > ./entregables/DEMO_AS41.TXT
echo 42 | python -X utf8 main.py > ./entregables/DEMO_AS42.TXT
echo 51 | python -X utf8 main.py > ./entregables/DEMO_AS51.TXT