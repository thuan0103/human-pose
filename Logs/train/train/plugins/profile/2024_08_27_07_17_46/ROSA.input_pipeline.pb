$	{�):�˿?����d��?��ǘ���?!���o_�?	ug��@���)Ŀ*@!���V*7@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$���o_�?Tt$����?A��3��?Y�=yX��?"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails��ǘ���?�����g?A��_�Lu?"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails*:��H�?=,Ԛ��?A��_�LU?*	�����\e@2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap#J{�/L�?!`�#��{I@)r�����?1�>�	��D@:Preprocessing2u
>Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map�'���?!a�TW�P=@)�� �rh�?1Ԣ�o	�3@:Preprocessing2F
Iterator::Model��q���?!ѫ9[�z/@)ˡE����?1íXp��'@:Preprocessing2�
LIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat?�ܵ�|�?!���g�"@)���Q��?1oS&ۍ!@:Preprocessing2w
@Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[16]::Concatenatelxz�,C|?!�#u�X&@)S�!�uq{?1�'��]@:Preprocessing2U
Iterator::Model::ParallelMapV2-C��6z?!6�����@)-C��6z?16�����@:Preprocessing2w
@Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[17]::Concatenate�����w?!�oS&@){�G�zt?1����g@:Preprocessing2p
9Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch��H�}m?!�;z� @)��H�}m?1�;z� @:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat"��u��q?!Ī<w� @)-C��6j?16������?:Preprocessing2Z
#Iterator::Model::ParallelMapV2::Zip�*��	�?!�C�}�xK@){�G�zd?1����g�?:Preprocessing2�
SIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat::Range/n��R?!���ʘ�?)/n��R?1���ʘ�?:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor/n��R?!���ʘ�?)/n��R?1���ʘ�?:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[17]::Concatenate[1]::FromTensora2U0*�C?!(���"x�?)a2U0*�C?1(���"x�?:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[16]::Concatenate[1]::FromTensor-C��6*?!6������?)-C��6*?16������?:Preprocessing2�
PIterator::Model::ParallelMapV2::Zip[0]::FlatMap[17]::Concatenate[0]::TensorSlice-C��6*?!6������?)-C��6*?16������?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
both�Your program is MODERATELY input-bound because 11.4% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*high2t65.3 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.9�|u��&@>Look at Section 3 for the breakdown of input time on the host.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
$	�
!����?��ʦ�;�?�����g?!=,Ԛ��?	!       "	!       *	!       2$	�b�꺝? � ��?��_�LU?!��3��?:	!       B	!       J	�!��u��?���?!�=yX��?R	!       Z	�!��u��?���?!�=yX��?JCPU_ONLYY�|u��&@b 