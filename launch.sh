# Asegura que la carpeta de entregables exista antes de lanzar los tests
mkdir -p entregables

echo AS11 | python -X utf8 main.py > ./entregables/DEMO_AS11.TXT
echo AS12 | python -X utf8 main.py > ./entregables/DEMO_AS12.TXT
echo AS13 | python -X utf8 main.py > ./entregables/DEMO_AS13.TXT
echo AS21 | python -X utf8 main.py > ./entregables/DEMO_AS21.TXT
echo AS22 | python -X utf8 main.py > ./entregables/DEMO_AS22.TXT
echo AS31 | python -X utf8 main.py > ./entregables/DEMO_AS31.TXT
echo AS41 | python -X utf8 main.py > ./entregables/DEMO_AS41.TXT
echo AS42 | python -X utf8 main.py > ./entregables/DEMO_AS42.TXT
echo AS51 | python -X utf8 main.py > ./entregables/DEMO_AS51.TXT


# echo AS11 | python -X utf8 main.py > .\entregables\DEMO_AS11.TXT
# echo AS12 | python -X utf8 main.py > .\entregables\DEMO_AS12.TXT
# echo AS13 | python -X utf8 main.py > .\entregables\DEMO_AS13.TXT
# echo AS21 | python -X utf8 main.py > .\entregables\DEMO_AS21.TXT
# echo AS22 | python -X utf8 main.py > .\entregables\DEMO_AS22.TXT
# echo AS31 | python -X utf8 main.py > .\entregables\DEMO_AS31.TXT
# echo AS41 | python -X utf8 main.py > .\entregables\DEMO_AS41.TXT