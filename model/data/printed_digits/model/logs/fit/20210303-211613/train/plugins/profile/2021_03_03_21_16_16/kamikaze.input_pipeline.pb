	?S^?9@?S^?9@!?S^?9@	b?	s???b?	s???!b?	s???"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$?S^?9@R?hE??A???b?9@YT1??c??*	"?rh??j@2F
Iterator::Model??D.8???!?gyújE@)?n??Ű?1?????>@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat???QF\??!P]ҭ??=@)?H?]۫?1??,?_9@:Preprocessing2S
Iterator::Model::ParallelMap?cZ?????!??G???(@)?cZ?????1??G???(@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate{?V??נ?!v?B???.@)?ek}?Ж?1r??a ?$@:Preprocessing2X
!Iterator::Model::ParallelMap::Zipˆ5?Ea??!X??<E?L@)??!?Q*??1t?(PE@:Preprocessing2?
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlice?f׽??!?????@)?f׽??1?????@:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor??~j?t??!j=?:θ@)??~j?t??1j=?:θ@:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMap?j???t??!???B?3@)?o?[t??1e=?G?@:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 0.6% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	R?hE??R?hE??!R?hE??      ??!       "      ??!       *      ??!       2	???b?9@???b?9@!???b?9@:      ??!       B      ??!       J	T1??c??T1??c??!T1??c??R      ??!       Z	T1??c??T1??c??!T1??c??JCPU_ONLY