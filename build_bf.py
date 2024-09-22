import argparse
from bloom_filter_handler import BloomFilterHandler



def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="load the database into bloom filter.")
    parser.add_argument('-i', '--input', required=True, help="path to reference sequences")
    parser.add_argument('-o', '--output', default="db_bloom", help="Output directory for bloom filter")
    parser.add_argument('--kmer_size', type=int, default=21, help="K-mer size (default: 21)")
    parser.add_argument('--error_rate', type=float, default=0.001, help="Bloom filter error rate (default: 0.001)")
    args = parser.parse_args()

    # 初始化 BloomFilterHandler 并加载数据库
    print("Loading reference database...")
    bloom_handler = BloomFilterHandler(kmer_size=args.kmer_size, factor=4)
    bloom_handler.load_database(args.input)
    print("Database loaded successfully.")

    BloomFilterHandler.save_bloom_filter(bloom_handler, args.output)


if __name__ == "__main__":
    main()
