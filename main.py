import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
from flask import Flask, jsonify, request
import glob
import os
import argparse

app = Flask(__name__)

@app.route('/home')
def home():
    input_files = glob.glob("/app/data/input/*")
    type = request.args.get('type')
    if type.lower() == "trigger":
        final_dict = {}
        for file in input_files:
            results, _ = ins.segmentImage(file, show_bboxes=True, output_image_name=f"/app/data/output/output_{os.path.basename(file)}")

            final_dict[file] = dict(results["object_counts"])
        return jsonify(final_dict)
    else:
        return jsonify({"status": "OK"})

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path",default="pointrend_resnet50.pkl")
    pargs = parser.parse_args()

    ins = instanceSegmentation()
    ins.load_model(pargs.model_path)
    app.run(host="0.0.0.0", port=8081)

