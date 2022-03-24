from Bio import Entrez, SeqIO
from Bio.Blast.Applications import*
import sys
import os
cwd=os.getcwd()

#genome_id = sys.argv[1]


Entrez.email = 'beatrizsilva@alunos.utfpr.edu.br'


def download_genome(genome_id):
    
    saida = open(cwd+'/database_ncbi/genome_'+str(genome_id)+'.gb','w')
    
    handle = Entrez.efetch(db='nuccore', id=genome_id, rettype='gb')
    seqRecord = SeqIO.read(handle, format='gb')
    handle.close()
    saida.write(seqRecord.format('gb'))
    saida.close()
    return True

def organize_data_genbank(genome_id):
    
    arq = open(cwd+'/database_ncbi/proteins_database.fasta', 'a')

    
    for rec in SeqIO.parse(cwd+'/database_ncbi/genome_'+str(genome_id)+'.gb', 'genbank'):
        if rec.features:
            for feature in rec.features:
                if (feature.type == "CDS") and ('protein_id' in feature.qualifiers):
                    arq.write('>'+feature.qualifiers['protein_id'][0]+' '+rec.description+'\n')
                    arq.write(feature.qualifiers['translation'][0]+'\n')
                    
    
    arq.close()



#list_id = ['AP018402.1', 'CP024203.1', 'CP033054.1', 'CP025079.1', 'CP000560.2', 'CP025079', 'CP003332.1', 'FN597644.1', 'CP011225.1', 'CP020102.1', 'AL009126', 'CP003747.1']
#'CP024203.1' 'CP033054.1'

list_id = ['AP018402.1', 'CP025079.1', 'CP000560.2', 'CP025079', 'CP003332.1', 'FN597644.1', 'CP011225.1', 'CP020102.1', 'AL009126', 'CP003747.1']

n=len(list_id)
k=1



for genome_id in list_id:
    print("\nIniciando o Download do Arquivo Genbank do Genoma {}...".format(genome_id))
    download_genome(genome_id)
    print("\n... \n\nDownload Concluído...")
    print("\n... \n\nOrganizando o Arquivo Fasta com as Sequências de Proteínas...")
    organize_data_genbank(genome_id)
    print("\n... \n\nOrganização Conclúida... {} de {}...".format(k,n))
    k+=1

print("\n... \n\nGerando os Arquivos do Banco de Dados do BLAST...")
makeblast=NcbimakeblastdbCommandline(dbtype='prot', input_file='database_ncbi/proteins_database.fasta', out='database_blastp/database_Bacillus')
makeblast()
print("\n... \n\nArquivos Gerados!\n\n")
    