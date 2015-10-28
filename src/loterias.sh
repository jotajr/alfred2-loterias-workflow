CONCURSO=$(python -c "import loterias; loterias.mega_concurso()")
MEGA=$(python -c "import loterias; loterias.mega_num_sorteados()")
GANHADORES=$(python -c "import loterias; loterias.mega_ganhadores()")
ACUMULADO=$(python -c "import loterias; loterias.mega_acumulada()")

cat << EOB
<?xml version="1.0"?>
<items>
  <item>
    <title>Mega Sena - $CONCURSO</title>
	  <subtitle>Números: $MEGA- $GANHADORES - $ACUMULADO</subtitle>
    <icon>mega_sena_icon.png</icon>
  </item>
</items>
EOB
