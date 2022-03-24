from Bio import Entrez, SeqIO
from Bio.Blast.Applications import*
import sys


#genome_id = sys.argv[1]

Entrez.email = 'beatrizsilva@alunos.utfpr.edu.br'


def download_genome(genome_id):
    
    saida = open('database_query/genome_'+str(genome_id)+'.gb','w')
    
    handle = Entrez.efetch(db='nuccore', id=genome_id, rettype='gb')
    seqRecord = SeqIO.read(handle, format='gb')
    handle.close()
    saida.write(seqRecord.format('gb'))
    saida.close()
    return True

def organize_data_genbank(genome_id):
    
    arq = open("database_query/proteins_"+str(genome_id)+".fasta", 'w')
    
    
    for rec in SeqIO.parse("database_query/genome_"+str(genome_id)+".gb", "genbank"):
        if rec.features:
            for feature in rec.features:
                if (feature.type == "CDS") and ('protein_id' in feature.qualifiers):
                    arq.write('>'+feature.qualifiers['protein_id'][0]+' '+rec.description+'\n')
                    arq.write(feature.qualifiers["translation"][0]+'\n')
    
    arq.close()


list_id = ['CP045993.1', 'CP023748.1', 'CP079719.1']

for genome_id in list_id:
    print("\nIniciando o Download do Arquivo Genbank do Genoma {}...".format(genome_id))
    download_genome(genome_id)
    print("\n... \n\nDownload Concluído...")
    print("\n... \n\nOrganizando o Arquivo Fasta com as Sequências de Proteínas...")
    organize_data_genbank(genome_id)
    print("\n... \n\nOrganização Conclúida... {} de {}...".format(k,n))
    k+=1
