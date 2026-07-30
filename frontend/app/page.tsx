import FileUpload from "@/components/FileUpload";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white shadow-xl rounded-2xl p-10 w-[700px] text-center">

        <h1 className="text-5xl font-bold text-blue-600">
          AI ML Workspace
        </h1>

        <p className="text-gray-600 mt-4 text-lg">
          Analyze your datasets with AI-powered insights
        </p>

        <div className="mt-10 border-2 border-dashed border-blue-400 rounded-xl p-12">

          <div className="text-6xl">
            📂
          </div>

          <h2 className="text-2xl font-semibold mt-4">
            Upload Dataset
          </h2>

          <p className="text-gray-500 mt-2">
            Drag & Drop your CSV file here
          </p>

          <FileUpload />

        </div>

      </div>
    </main>
  );
}