from flask import Flask, request, jsonify
from fastapi import FastAPI, Query
from CrawlAI.Tree_Gen import run_advanced_crawler
from CrawlAI.UI_Gen import deep_crawl
from CrawlAI.Intent_Gen import process_all_files
from pydantic import BaseModel
import json
import os 
import stat
import shutil
import traceback

from flask import Flask, request, jsonify
import asyncio

app = Flask(__name__)

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
print(f"src path {src_dir} ")

def clear_folder(folder_path):
    """Delete all files in the specified folder."""
    if not os.path.exists(folder_path):
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.chmod(file_path, stat.S_IWRITE)  
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, onerror=lambda func, path, excinfo: os.chmod(path, stat.S_IWRITE) or func(path))
        except Exception as e:
            print(f"Warning: impossible to delete {file_path}. Reason: {e}")
            traceback.print_exc()


@app.route("/full_tree", methods=['POST'])
def full_tree():
    try:
        data = request.get_json()
        url = data.get("url")
        max_depth = int(data.get("max_depth", 2))

        result = asyncio.run(run_advanced_crawler(url, max_depth))
        dir=os.path.join(src_dir, "outputs", "tree")
        os.makedirs(dir, exist_ok=True)

        clear_folder(dir)

        with open(os.path.join(dir, "full_output_tree.json"), "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        response= {
            "message": "Tree successfully generated",
            "tree": result
        }

        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/deep_crawl", methods=["POST"])
def crawl_deep():
    '''This endpoint accepts a JSON playload with max_depth and urls that is a list of strings, the first string is the parent url, the other strings are the child urls to be selected for the deep crawl.
    If only one url is provided, the deep crawl will be performed for all the urls found up to the specified depth.'''
    
    try:
        data=request.get_json()
        urls=data.get("urls")
        mode=data.get("mode")
        #depth=int(data.get("max_depth", 2))

        if not urls or not isinstance(urls, list,):
            return jsonify({"error": "Field 'urls' must be a list of URLs"}), 400
        
        asyncio.run(deep_crawl(urls, mode))
        #asyncio.run(deep_crawl(urls, depth))

        return jsonify({"message": "The tree successfully created."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/gen_intents", methods=["POST"])
def gen_intents():
    try:
        results=asyncio.run(process_all_files())
        return jsonify({"message": f"Instructions successfully created."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)