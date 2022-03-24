from Bio.Blast.Applications import*
import os
cwd=os.getcwd()


print("\nIniciando a Pesquisa BLAST com as Sequências de Proteínas...")

caminho_db = str(cwd)+"/database_blastp/database_Bacillus"

sequence_list = ['CP045993.1', 'CP023748.1', 'CP079719.1']

n=len(sequence_list)
k=1

for sequence in sequence_list:
	print("\n... \n\nPesquisa BLAST iniciada... {} de {}...\n".format(k,n))
	comando_blastp = NcbiblastpCommandline(query=cwd+"/database_query/proteins_"+str(sequence)+".fasta", db=caminho_db, out=cwd+"/resultado_blastp/Resultado_Blastp_"+str(sequence)+".out")
	print(comando_blastp)
	stdout,stderr = comando_blastp()
	print("\n... \n\nPesquisa BLAST {} de {} Conclúida...".format(k,n))
	k+=1


print("\n\nPesquisa BLAST Conclúida!\n\n")