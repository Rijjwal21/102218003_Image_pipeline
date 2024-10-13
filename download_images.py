from icrawler.builtin import GoogleImageCrawler
import argparse
import os

def crawl_images(keyword, max_num, storage_dir):
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    
    crawler = GoogleImageCrawler(storage={'root_dir': storage_dir})
    crawler.crawl(keyword=keyword, max_num=max_num)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl and download images from Google.")
    parser.add_argument("keyword", type=str, help="Keyword for image search.")
    parser.add_argument("max_num", type=int, help="Maximum number of images to download.")
    parser.add_argument("storage_dir", type=str, help="Directory to save the images.")
    
    args = parser.parse_args()
    
    crawl_images(args.keyword, args.max_num, args.storage_dir)



    