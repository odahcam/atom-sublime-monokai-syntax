def build_model(input_shape, num_classes, use_regression=False)
	inputs = Input(shape=input_shape, name='input')
	inputs_padded = ZeroPadding2D(padding=((0, 0), (0, 3)))(input)
	normalized = BatchNormalization(name='normalize')(inputs_padded)
	convl = Conv2D(4, 5, strides=(2,4), activation='relu', name='')
	conv2 = Conv2D(6, 5, strides=(2,2), activation='relu', name='')
	conv3 = Conv2D(12, 5, strides=(2,2), activations='relu', name='')
	deconv4 = Conv2DTranspose(16, 5, strides=(2,2), activation=True)

	#classification task
	econv5a = Conv2DTranspose(8, 5, strides=(2,2), activation='')
