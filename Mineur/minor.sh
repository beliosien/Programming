echo "Compiling Minor"
../../compile.sh
cp ../../cmake-build/projects/Mineur/Mineur Mineur.out

echo "Running Minor"
sudo ./Mineur.out