CONCURSO_MEGA=$(python -c "import loterias; loterias.mega_concurso()")
MEGA=$(python -c "import loterias; loterias.mega_num_sorteados()")
GANHADORES_MEGA=$(python -c "import loterias; loterias.mega_ganhadores()")
ACUMULADO_MEGA=$(python -c "import loterias; loterias.mega_acumulada()")

CONCURSO_QUINA=$(python -c "import loterias; loterias.quina_concurso()")
QUINA=$(python -c "import loterias; loterias.quina_num_sorteados()")
GANHADORES_QUINA=$(python -c "import loterias; loterias.quina_ganhadores()")
ACUMULADO_QUINA=$(python -c "import loterias; loterias.quina_acumulada()")

CONCURSO_FEDERAL=$(python -c "import loterias; loterias.federal_concurso()")
FEDERAL=$(python -c "import loterias; loterias.federal_premios()")

cat << EOB
<?xml version="1.0"?>
<items>
  <item>
    <title>Mega Sena - $CONCURSO_MEGA</title>
	  <subtitle>Números: $MEGA- $GANHADORES_MEGA - $ACUMULADO_MEGA</subtitle>
    <icon>mega_sena_icon.png</icon>
  </item>
  <item>
    <title>Quina - $CONCURSO_QUINA</title>
	  <subtitle>Números: $QUINA- $GANHADORES_QUINA - $ACUMULADO_QUINA</subtitle>
    <icon>quina_icon.png</icon>
  </item>
  <item>
    <title>Loteria Federal - $CONCURSO_FEDERAL</title>
	  <subtitle>Prêmios: $FEDERAL</subtitle>
    <icon>federal_icon.png</icon>
  </item>
</items>
EOB
