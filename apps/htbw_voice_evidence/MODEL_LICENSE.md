# Model licence and attribution

The BehavesWell Voice Evidence App uses one third-party model artifact. It is **not** stored in
this repository or in the App image; the App downloads it at runtime from a
revision-pinned URL into its private `/data` directory and verifies its SHA-256 digest
before every use.

| Field | Value |
| --- | --- |
| Artifact | `voxceleb_ECAPA512_LM.onnx` |
| Source | Hugging Face repository [`Wespeaker/wespeaker-ecapa-tdnn512-LM`](https://huggingface.co/Wespeaker/wespeaker-ecapa-tdnn512-LM) |
| Revision (commit) | `a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b` |
| SHA-256 | `d71b85d9b48058ef68004f04f1b78acebefb9dfcf542e19b976a12a5ad1f10b0` |
| Size | 24,861,931 bytes |
| Download URL | <https://huggingface.co/Wespeaker/wespeaker-ecapa-tdnn512-LM/resolve/a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b/voxceleb_ECAPA512_LM.onnx> |
| Licence | Creative Commons Attribution 4.0 International (CC BY 4.0), as declared in the model card of this repository at this revision |
| Licence text | <https://creativecommons.org/licenses/by/4.0/> |
| Model card | <https://huggingface.co/Wespeaker/wespeaker-ecapa-tdnn512-LM/blob/a2f3dcb1c8702caccc7a55ceb57f5e8d1842112b/README.md> |

## Attribution

"voxceleb_ECAPA512_LM.onnx" (ECAPA-TDNN based speaker embedding model, after large-margin
fine-tuning, trained on VoxCeleb2 Dev) is provided by the
[WeSpeaker](https://github.com/wenet-e2e/wespeaker) project and is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The App uses the artifact
unmodified.

The model card asks users to cite:

- B. Desplanques, J. Thienpondt, K. Demuynck, "ECAPA-TDNN: Emphasized Channel Attention,
  Propagation and Aggregation in TDNN Based Speaker Verification", arXiv:2005.07143, 2020.
- H. Wang, C. Liang, S. Wang, Z. Chen, B. Zhang, X. Xiang, Y. Deng, Y. Qian, "WeSpeaker: A
  Research and Production Oriented Speaker Embedding Learning Toolkit", ICASSP 2023.

The licence above is the licence of this model artifact as declared on its model card; it
is not inferred from the licence of the WeSpeaker toolkit source code. The App's own
feature extraction is an independent NumPy implementation of the Kaldi-compatible
filterbank that WeSpeaker uses at inference; no WeSpeaker source code is included.
