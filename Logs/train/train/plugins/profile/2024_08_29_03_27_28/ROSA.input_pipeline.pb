$	!�rh���?��&;��?�HP��?!��1�%�?	m2�4=@� ్"@!m2�4=*@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$��1�%�?�Zd;�?AvOjM�?Ym���{�?"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails�HP��?U���N@s?A���Q�~?*	�����Yq@2F
Iterator::Modela��+e�?!��LHzH@)	�^)��?1'QV��G@:Preprocessing2f
/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap$(~��k�?!�3N���A@)/�$���?1�Q�J��;@:Preprocessing2u
>Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map]m���{�?!��6*@)M�St$�?1��LH @:Preprocessing2�
LIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat���S㥋?!
v ��s@)-C��6�?1�\&$�q@:Preprocessing2w
@Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[16]::Concatenatea2U0*��?!p�9�k�@)U���N@�?1�X��@:Preprocessing2w
@Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[17]::Concatenate��ׁsF�?!�W���@)�&S��?1,�fo�9
@:Preprocessing2U
Iterator::Model::ParallelMapV2U���N@s?!�X���?)U���N@s?1�X���?:Preprocessing2p
9Iterator::Model::ParallelMapV2::Zip[0]::FlatMap::PrefetchF%u�k?!ݏG*�?)F%u�k?1ݏG*�?:Preprocessing2l
5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat/n��r?!ѿ�8\�?)-C��6j?1�\&$�q�?:Preprocessing2Z
#Iterator::Model::ParallelMapV2::ZipF%u��?!ݏG*C@)ŏ1w-!_?1c�����?:Preprocessing2x
AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensora2U0*�S?!p�9�k��?)a2U0*�S?1p�9�k��?:Preprocessing2�
SIterator::Model::ParallelMapV2::Zip[0]::FlatMap::Prefetch::Map::FiniteRepeat::RangeǺ���F?!V��i#�?)Ǻ���F?1V��i#�?:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[17]::Concatenate[1]::FromTensora2U0*�C?!p�9�k��?)a2U0*�C?1p�9�k��?:Preprocessing2�
OIterator::Model::ParallelMapV2::Zip[0]::FlatMap[16]::Concatenate[1]::FromTensor-C��6*?!�\&$�q�?)-C��6*?1�\&$�q�?:Preprocessing2�
PIterator::Model::ParallelMapV2::Zip[0]::FlatMap[17]::Concatenate[0]::TensorSlice-C��6*?!�\&$�q�?)-C��6*?1�\&$�q�?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
both�Your program is MODERATELY input-bound because 12.5% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*high2t70.4 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.9RvLB)@>Look at Section 3 for the breakdown of input time on the host.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
$	�A�fշ?r�2<� �?U���N@s?!�Zd;�?	!       "	!       *	!       2$	M�St$�?ʨe��ݕ?���Q�~?!vOjM�?:	!       B	!       J	m���{�?bc2����?!m���{�?R	!       Z	m���{�?bc2����?!m���{�?JCPU_ONLYYRvLB)@b 