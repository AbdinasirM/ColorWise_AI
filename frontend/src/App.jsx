import React, { useState } from 'react';

function App() {

  async function proccessImage(image) {
    const url = "http://192.168.1.19:8000/imageprocessing";
    
    // Prepare the form data
    const formData = new FormData();
    formData.append('file', image);

    try {
      const response = await fetch(url, {
        method: 'POST',
        body: formData,
      });

      const result = await response.json();
      console.log(result);
      
    } catch (error) {
      console.log(error);
    }
  }
  
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [isUploading, setIsUploading] = useState(false);

  const handleFileChange = (event) => {
    const files = Array.from(event.target.files);
    setSelectedFiles(files);
  };

  const handleUpload = () => {
    if (selectedFiles.length > 0) {
      setIsUploading(true);
      setUploadProgress(0);

      // Simulate a file upload process
      const uploadInterval = setInterval(() => {
        setUploadProgress((prevProgress) => {
          if (prevProgress >= 100) {
            clearInterval(uploadInterval);
            setIsUploading(false);

            // Trigger image processing after simulated upload is complete
            selectedFiles.forEach((file) => {
              proccessImage(file);
            });

            return 100;
          }
          return prevProgress + 10;
        });
      }, 300);
    }
  };

  const handleRemoveImage = (index) => {
    const newFiles = [...selectedFiles];
    newFiles.splice(index, 1);
    setSelectedFiles(newFiles);
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100 p-6">
      <div className="w-full max-w-2xl p-10 space-y-6 bg-white rounded-lg shadow-lg">
        <div className="flex flex-col items-center justify-center space-y-6">
          <div
            className={`w-full p-8 text-center border-dashed border-2 rounded-lg bg-gray-50`}
          >
            <input
              id="file-upload"
              type="file"
              multiple
              className="hidden"
              onChange={handleFileChange}
            />
            <label
              htmlFor="file-upload"
              className="block text-sm font-medium text-gray-700 cursor-pointer"
            >
              <svg
                className="mx-auto h-12 w-12 text-gray-400"
                stroke="currentColor"
                fill="none"
                viewBox="0 0 48 48"
                aria-hidden="true"
              >
                <path
                  d="M14.5 20.5l9.5 9.5m0 0l9.5-9.5m-9.5 9.5V6m14 31h-28a2 2 0 01-2-2V16a2 2 0 012-2h6.5"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
              <span className="text-blue-600">Click to upload</span> or drag and drop
            </label>
          </div>

          {selectedFiles.length > 0 && (
            <div className="w-full space-y-2">
              {selectedFiles.map((file, index) => (
                <div key={index} className="flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <img
                      src={URL.createObjectURL(file)}
                      alt={file.name}
                      className="w-20 h-20 object-cover rounded-md"
                    />
                    <span className="text-sm text-gray-700">{file.name}</span>
                  </div>
                  <button
                    className="text-red-600 hover:underline text-sm"
                    onClick={() => handleRemoveImage(index)}
                  >
                    Remove
                  </button>
                </div>
              ))}
            </div>
          )}

          {isUploading && (
            <div className="w-full bg-gray-200 rounded-full h-2.5 mt-4">
              <div
                className="bg-blue-600 h-2.5 rounded-full"
                style={{ width: `${uploadProgress}%` }}
              ></div>
            </div>
          )}

          <button
            onClick={handleUpload}
            className={`w-full py-3 px-6 bg-green-600 text-white rounded-lg shadow hover:bg-green-700 focus:outline-none ${
              isUploading || selectedFiles.length === 0 ? 'opacity-50 cursor-not-allowed' : ''
            }`}
            disabled={isUploading || selectedFiles.length === 0}
          >
            {isUploading ? 'Uploading...' : 'Upload Files'}
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
