?	???`?tN@???`?tN@!???`?tN@	l|bt?X??l|bt?X??!l|bt?X??"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$???`?tN@y7R???A|G?	1!N@Y??n?!??*	?$???x@2F
Iterator::Model?G??|???!?7f??`Q@)o??o?D??1
9Q?F?N@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat?????H??!T??KX?,@)??????1ʸ@Pc'@:Preprocessing2S
Iterator::Model::ParallelMapb?k_@??!0?????@)b?k_@??10?????@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenateb?G??!?{???#@)?bG?P???1>i?[pj@:Preprocessing2X
!Iterator::Model::ParallelMap::Zip?}?֤۾?!!gf@}>@)/???uR??1L?l
??@:Preprocessing2?
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice3?FY????!Wa??~N@)3?FY????1Wa??~N@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor??4c?t??!?S+ 0@)??4c?t??1?S+ 0@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMap3?FY????!Wa??~N(@)o?EE?N??1?Q?D?@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.5% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	y7R???y7R???!y7R???      ??!       "      ??!       *      ??!       2	|G?	1!N@|G?	1!N@!|G?	1!N@:      ??!       B      ??!       J	??n?!????n?!??!??n?!??R      ??!       Z	??n?!????n?!??!??n?!??JCPU_ONLY2black"?
device?Your program is NOT input-bound because only 0.5% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2I
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono:
Refer to the TF2 Profiler FAQ2"CPU: 